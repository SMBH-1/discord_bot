import React from "react";
import Container from "react-bootstrap/Container";
function CommandTable() {
  const general = {
    name: "General",
    commands: [
      [
        "!win",
        "generates a random lottery number based on data collected from all MegaMillion's winning numbers",
        "",
        "",
      ],
      ["!latest draw", "returns the last drawn winning numbers", "", ""],
      ["!help", "view all available commands", "", ""],
      ["!hello", "receive a wonderful greeting", "", ""],
      ["!meow", "generate a random cat picture", "", ""],
      [
        "!lookup {character name} {server}",
        "check WoW for Gladiator achievement",
        "character name, server",
        "",
      ],
    ],
  };
  const chatGPT = {
    name: "ChatGPT",
    commands: [
      ["!chatbot", "Engage the bot", "", ""],
      ["!helpbot", "List all commands for chatbot as an embed", "", ""],
      ["!server", "Displays some server stats", "", ""],
    ],
  };
  const music = {
    name: "Music",
    commands: [
      ["/help", "lists all slash commands", "", ""],
      [
        "/play",
        "searches youtube with input search terms, puts song in queue",
        "search terms",
        "",
      ],
      ["/queue", "displays currently playing song and songs in queue", "", ""],
      ["/pause", "pauses current song in queue", "", ""],
      ["/resume", "resumes playing current song from queue", "", ""],
      ["/skip", "skips current song", "", ""],
      ["/clear", "clears current queue", "", ""],
      ["/leave", "kicks bot from current voice channel", "", ""],
      [
        "!create_playlist",
        "Create a playlist associated with your account",
        "",
        "",
      ],
      [
        "!list_playlists",
        "Lists all playlists associated with your account",
        "",
        "",
      ],
      [
        "!list_songs",
        "Lists all songs within a playlist",
        "!list_songs {playlist name}",
        "",
      ],
      [
        "!add",
        "Add a song to a playlist, you must add the youbtube URL",
        "!add {youtubeURL} to {playlist name}",
        "",
      ],
      [
        "!delete_song",
        "Delete a song from your playlist",
        "!delete_song {youtubeURL from {playlist name}",
        "",
      ],
      [
        "!delete_playlist",
        "Delete an entire playlist",
        "!delete_playlist {playlist name}",
        "",
      ],
      [
        "/playlist",
        "Play a playlist from youtube",
        "/playlist {playlist name}",
        "",
      ],
    ],
  };
  const dnd = {
    name: "Dungeons & Dragons",
    commands: [
      [
        "!roll xdy",
        "roll",
        "x = number of dice, y = max value of die, ie. 2d6 or 6d12)",
        "alias = !r",
      ],

      [
        "!init -mod/+mod (ie. +3 or -1)",
        "roll initiative",
        "initiative modifier for the user's player-character",
        "alias = !i",
      ],

      [
        "!dm_init <NPC:str> +/-int",
        "roll initiative for non-player character",
        "npc_id string, initiative modifier",
        "alias = !di",
      ],

      [
        "!run_init",
        "sorts, prints, and then clears out the initiative roll pool",
        "",
        "alias = !run/!ri",
      ],
      [
        "!condition <search_term:str>",
        "returns the rules regarding the input condition",
        "search term",
        "",
      ],
      [
        "!condition list",
        "return a list of all valid conditions/search-terms)",
        "",
        "aliases = !cond/!c",
      ],
    ],
  };

  const masterList = [music, general, chatGPT, dnd];
  return (
    <Container>
      <table className="table table-hover">
        {masterList.map((category) => (
          <>
            <thead key={category.name}>
              <tr className="table-info">
                <th scope="col">{category.name}</th>
                <th scope="col"></th>
                <th scope="col"></th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr className="table-active">
                <th scope="col">Command</th>
                <th scope="col">Description</th>
                <th scope="col">Arguments</th>
                <th scope="col">Alias</th>
              </tr>

              {category.commands.map((command, i) => (
                <tr key={i}>
                  {command.map((data, i) => (
                    <td key={i}>{data}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </>
        ))}
      </table>
    </Container>
  );
}

export default CommandTable;
